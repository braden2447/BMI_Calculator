# BMI Calculator 

def bmi_data_input():
    print('Welcome to the BMI Calculator!')
    print('You can input your body measurements below in units of kilograms/meters or pounds/inches')
    print('Example:')
    print('Weight: 185 pounds')
    print('Height: 72 inches')
    print('Now, please enter your information below.')
    weight = input('Weight: ')
    weight = float(weight)
    height = input('Height: ')
    height = float(height)
    return weight, height
    
def main():
    bmi_data_input()

if __name__ == '__main__'
    main()
    
          