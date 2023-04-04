from tkinter import*

root=Tk()
root.title('driving licence')

root.geometry('400x200') 
root.configure(background="somkewhite")

label_heading=Label(root)
label_id_tag=Label(root)
label_name_tag=Label(root)
label_dob_tag=Label(root)
label_pin_tag=Label(root)
label_address_tag=Label(root)
label_vehicle_type_tag=Label(root)

label_heading['text']= "Driving License"
label_id_tag['text']= "ID : 218245223552"
label_name_tag['text']= "Name :gejuic"
label_dob_tag['text']= "Date of birth :28 . 9 . 2048"
label_pin_tag['text']= "Pin no. : 924 457"
label_address_tag['text'] = "Address : disney land,  Hong Kong"
label_vehicle_type_tag['text'] = "Authorisation to drive the following vehicles : two , four"

label_heading.pack()
label_id_tag.pack()
label_name_tag.pack()
label_dob_tag.pack()
label_pin_tag.pack()
label_address_tag.pack()
label_vehicle_type_tag.pack()


root.mainloop()