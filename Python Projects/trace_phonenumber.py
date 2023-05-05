import phonenumbers as pn
from phonenumbers import timezone,geocoder,carrier
# from phonenumbers.util import prnt

p_number = input("Enter the phone number with country code:")

number = pn.parse(p_number)
# prnt(x)

time_zone = timezone.time_zones_for_number(number)
car = carrier.name_for_number(number,"en")
reg = geocoder.description_for_number(number,"en")

print(number)
print(f"The Timezone of your Mobile number is : {time_zone}")
print(f"The Number is of : {car}")
print(f"It is from : {reg}")

# formater = pn.AsYouTypeFormatter("IND")
# prnt(formater.input_digit("8"))
