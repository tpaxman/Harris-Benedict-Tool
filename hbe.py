ACTIVITY_LEVELS = {
    1: {'factor': 1.200, 'descrip': 'sedentary'},
    2: {'factor': 1.375, 'descrip': 'lightly active'},
    3: {'factor': 1.550, 'descrip': 'moderately active'},
    4: {'factor': 1.700, 'descrip': 'very active'},
    5: {'factor': 1.900, 'descrip': 'extremely active'},
}

GENDER_COEFFICIENTS = {
    'm': {'const': 66, 'weight': 6.23, 'height': 12.7, 'age': 6.8},
    'f': {'const': 655, 'weight': 4.35, 'height': 4.7, 'age': 4.7},
}


def main():
    # get attributes
    get_number = lambda msg: input_extended(msg, float, lambda x: x > 0)

    height_inch = get_number('Height in inches: ')
    weight_lbs = get_number('Weight in pounds: ')
    age_years = get_number('Age in years: ')
    gender = input_extended('Enter your gender (m or f): ',
                            criteria=lambda x: x in GENDER_COEFFICIENTS.keys())

    descriptions = {k: v['descrip'] for k, v in ACTIVITY_LEVELS.items()}
    descrip_strings = [f'{k} = {v}' for k, v in descriptions.items()]
    all_descrips = '\n'.join(['How active are you?'] + descrip_strings) + '\n'
    activity = input_extended(all_descrips, int, lambda x: x in ACTIVITY_LEVELS.keys())

    # Calculations
    bmr = calc_bmr(gender, weight_lbs, height_inch, age_years)
    calories_burned = calc_calories_burned(bmr, activity)

    print("Your BMR is " + str(bmr))
    print("You burn " + str(calories_burned) + " calories per day.")


def calc_bmr(gender, weight_lbs, height_inch, age_years):
    coefs = GENDER_COEFFICIENTS.get(gender)
    bmr = (coefs['const']
           + coefs['weight'] * weight_lbs
           + coefs['height'] * height_inch
           - coefs['age'] * age_years)
    return bmr


def calc_calories_burned(bmr, activity):
    activity_factor = ACTIVITY_LEVELS[activity]['factor']
    return bmr * activity_factor


def input_extended(prompt, cast_to=None, criteria=None):

    # verify the function inputs
    assert isinstance(prompt, str)

    if cast_to:
        assert callable(cast_to), 'Cast_to must be callable'
        assert isinstance(cast_to, type), 'Cast_to must be a type'

    if criteria:
        assert callable(criteria), 'Criteria must be callable'

    # keep requesting input until a valid value is given
    while True:

        raw_value = input(prompt)

        # cast input value to some type
        if not cast_to:
            casted_value = raw_value
        else:
            try:
                casted_value = cast_to(raw_value)
            except ValueError:
                print(f'Cannot cast input to {str(cast_to)}')
                continue  # skip the rest, loop again

        # check if the input is valid based on criteria function
        if not criteria:
            return casted_value
        else:
            is_valid = criteria(casted_value)
            assert isinstance(is_valid, bool), 'Validate_func must return bool'
            if is_valid:
                validated_value = casted_value
                break
            else:
                print('Invalid entry')
                continue

    return validated_value


if __name__ == '__main__':
    main()
