import json

from utils.exceptions import FormLengthException, FormTypeException,\
    FormValidationException, InvalidFormException, NotProvideException


class Request:

    @classmethod
    def body_validation(cls, form=[]):
        def decorator(func):
            def wrapper(request, *args, **kwargs):
                body_data = request.body
                try:
                    data = json.loads(body_data)
                except json.decoder.JSONDecodeError:
                    return InvalidFormException()

                for key in form:
                    try:
                        item = data.get(key)
                        if form[key]['required'] is False and not item:
                            continue

                        elif form[key]['required'] and not isinstance(item, bool) and not item:
                            return NotProvideException(message=f'Not provide a {key} in body request')

                    except TypeError:
                        return NotProvideException(message=f'Not provide a {key} in body request')

                    if not cls.is_valid_type(item, form[key]['type']):
                        return FormTypeException(message=f'The type of {key} must be {form[key]["type"]}')

                    if form[key]['max_length']:
                        if not cls.is_valid_length(
                            assert_length=form[key]['max_length'],
                            data=item,
                        ):
                            return FormLengthException(message=f'طول {form[key]["field_name"]} بیش از حد مجاز است')

                    if callable(form[key].get('validator')):
                        if not form[key].get('validator')(item):
                            return FormValidationException(message=f'فرمت {form[key].get("field_name")} معتبر نیست')

                kwargs['body'] = data
                return func(request, *args, **kwargs)
            return wrapper
        return decorator

    @classmethod
    def is_valid_type(cls, data, assert_type):
        return isinstance(data, assert_type)

    @classmethod
    def is_valid_length(cls, assert_length, data):
        if isinstance(data, list):
            return assert_length >= len(data)

        return assert_length >= len(str(data))
