from tkinter import *
from random import randint
from numpy import intp

def nutritionwindow():
    def BMR(w,h,age,act,gender):

        protein = ['Yogurt(1 cup)','Cooked meat(3 Oz)','Cooked fish(4 Oz)','1 whole egg + 4 egg whites','Tofu(5 Oz)']
        fruit = ['Berries(80 Oz)','Apple','Orange','Banana','Dried Fruits(Handfull)','Fruit Juice(125ml)']
        vegetable = ['Any vegetable(80g)']
        grains = ['Cooked Grain(150g)','Whole Grain Bread(1 slice)','Half Large Potato(75g)','Oats(250g)','2 corn tortillas']
        ps = ['Soy nuts(i Oz)','Low fat milk(250ml)','Hummus(4 Tbsp)','Cottage cheese (125g)','Flavored yogurt(125g)']
        taste_en = ['2 TSP (10 ml) olive oil','2 TBSP (30g) reduced-calorie salad dressin','1/4 medium avocado','Small handful of nuts','1/2 ounce  grated Parmesan cheese','1 TBSP (20g) jam, jelly, honey, syrup, sugar']

        # w = v3.get()
        # h = v4.get()
        # age = v5.get()
        # act = str(Lb.get(ACTIVE))
        # gender = Lb2.get(ACTIVE)

        if gender == 1:
            ncal = float()
            ncal = 88.362 + (13.397*float(w)) + (4.799*float(h)) - (5.677*float(age))
            print ("old calories",ncal)
        elif gender == 2:
            ncal = float()
            ncal = 447.593 + (9.247*float(w)) + (3.098*float(h)) - (4.330*float(age))


        if act == 1:
            cal = ncal*1.2

        elif act == 2:
            cal = ncal*1.375

        elif act == 3:
            cal = ncal*1.55

        elif act == 4:
            cal = ncal*1.725

        elif act == 5:
            cal = ncal*1.9

        print ("new calories",cal)


        if cal<1500:
           
            print("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)])

            print("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
  
            print("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
 
            print("Dinner: "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])

            print("Snack: "+fruit[randint(0, 5)])
     


        elif cal<1800:
  
            print("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)])
    
            print("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
     
            print("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
      
            print("Dinner: 2 "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
     
            print("Snack: "+fruit[randint(0, 5)])
   

        elif cal<2200:
        
            print("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)])
       
            print("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
        
            print("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        
            print("Dinner: 2 "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        
            print("Snack: "+fruit[randint(0, 5)])
        


        elif cal>=2200:
           
            print("Breakfast: 2 "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)]+" + "+grains[randint(0,4)])
            
            print("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
            
            print("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
            
            
            print("Dinner: 2 "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens + 2 "+grains[randint(0,4)]+" + 2 "+taste_en[randint(0,5)])
           
            print("Snack: "+fruit[randint(0, 5)])
          

  

 
    print("Your Dietitian is here!")
    print("Please enter your weight in kgs")
    weight = float(input())
    print("Please enter your height in cms")
    height = float(input())
    print("Please enter your age")
    age = float(input())
    print("Please enter your gender: Enter 1 for Male and 2 for female ")
    gender = int(input())
    print("ENTER 1 for Sedentary little or no exercise \n Enter 2 for Lightly active \(1-3 days/week\) \n ENTER 3 for Moderately active \(3-5 days/week\) \n ENTER 4 for Very active (6-7 days/week) \n ENTER 5 for Super active (twice/day)")
    exercise = int(input())

    BMR(weight,height,age,exercise,gender)

