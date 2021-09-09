# BMI Calculator 

def bmi_data_input():
    print('Welcome to the BMI Calculator!')
    print('You can input your body measurements below in units of kilograms/meters or pounds/inches')
    print('Example:')
    print('Weight: 185 pounds')
    print('Height: 72 inches')
    print('Now, please enter your information below.')
    weight = input('Weight: ')
    height = input('Height: ')
    return weight, height
    
def bmi_data_manipulation(weight, height):
    wt = weight.split(' ')
    wt[0] = float(wt[0])
    ht = height.split(' ')
    ht[0] = float(ht[0])    
    return wt, ht
    
def main():
    weight, height = bmi_data_input()
    wt, ht = bmi_data_manipulation(weight, height)
        

if __name__ == '__main__':
    main()
    
          