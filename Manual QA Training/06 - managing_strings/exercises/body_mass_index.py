def BMI(weight, height):
    # Split weight to allow conversion
    weight_values = weight.split(' ')
    weight_value = float(weight_values[0])
    weight_type = weight_values[1]

    # Split height to allow conversion
    height_values = height.split(' ')
    height_value = float(height_values[0])
    height_type = height_values[1]

    # Weight conversion
    if weight_type == 'pounds':
        # 1 lb == 0.45359237 kg
        weight = float(weight_value) * 0.45359237
    else:
        weight = float(weight_value)

    # Height conversion
    if height_type == 'inches':
        # 1 inch = 0.0254 meter
        height = float(height_value) * 0.0254
    else:
        height = float(height_value)

    # BMI calculation
    bmi_total = weight / (height ** 2)
    bmi_total = round(bmi_total, 1)

    # Display BMI result
    if bmi_total < 18.5:
        print(str(bmi_total) + ' - Underweight')
    elif 18.5 < bmi_total < 24.9:
        print(str(bmi_total) + ' - Normal Weight')
    elif 25 < bmi_total < 29.9:
        print(str(bmi_total) + ' - Overweight')
    else:
        print(str(bmi_total) + ' - Obesity')


BMI('205 pounds', '73 inches')
BMI('55 kilos', '1.65 meters')
BMI('154 pounds', '2 meters')
