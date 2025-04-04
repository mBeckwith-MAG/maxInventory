from utils.validate import not_empty, validate_length, validateAlphaNumeric, validateFloat, validateInt, validateString
from utils.classes import Vehicle
import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("M.I.M. | Max Inventory Management")
    root.geometry("600x400")

    main_layout = ttk.Notebook(root)
    main_layout.pack(fill=tk.BOTH, expand=True)

    veh_frame = ttk.Frame(main_layout)
    cust_frame = ttk.Frame(main_layout)
    form_frame = ttk.Frame(main_layout)

    main_layout.add(veh_frame, text="VEHICLES")
    main_layout.add(cust_frame, text="CUSTOMERS")
    main_layout.add(form_frame, text="FORMS")

    veh_frame_col_lft = tk.Frame(veh_frame)
    veh_frame_col_lft.pack(padx=0, pady=0)

    add_veh_btn = ttk.Button(veh_frame_col_lft, text="ADD", command=add_veh)
    add_veh_btn.pack(padx=20, pady=20)

    edit_veh_btn = ttk.Button(veh_frame_col_lft, text="EDIT", command=edit_veh)
    edit_veh_btn.pack(padx=20, pady=20)

    rem_veh_btn = ttk.Button(veh_frame_col_lft, text="REMOVE", command=rem_veh)
    rem_veh_btn.pack(padx=20, pady=20)

    veh_test_label = tk.Label(veh_frame, text="This is the Vehicle Tab")
    veh_test_label.pack(padx=20, pady=20)
    cust_test_label = tk.Label(cust_frame, text="This is the Customer Tab")
    cust_test_label.pack(padx=20, pady=20)
    form_test_label = tk.Label(form_frame, text="This is the Form Tab")
    form_test_label.pack(padx=20, pady=20)

    root.mainloop()



def add_veh():
    print("ADDING A VEHICLE!")

def edit_veh():
    print("EDITING A VEHICLE!")

def rem_veh():
    print("REMOVING A VEHICLE!")



if __name__ == "__main__":

    # Testing Validations
    vin = "SALCL2FX4RH346788"
    make = "Porsche"
    model = "911"
    year = 1999
    odo = 123
    cost = 123030.00

    vehicles = []

    if(not_empty(vin) and validateAlphaNumeric(vin) and validate_length(vin, 17)):
        if(not_empty(make) and validateString(make)):
            if(not_empty(model) and validateAlphaNumeric(model)):
                if(not_empty(year) and validateInt(year)):
                    if(not_empty(odo) and validateInt(odo)):
                        if(not_empty(cost) and validateFloat(cost)):
                            vehicles.append(Vehicle(vin, make, model, year, odo, cost))

    for vehicle in vehicles:
        vehicle.add_repair("Test Repair1", 252.36)
        vehicle.add_repair("Test Repair2", 52.3)
        vehicle.add_repair("Test Repair3", 25.6)
        vehicle.add_repair("Test Repair4", 2.36)
        print(vehicle)
        vehicle.show_repairs()

    
    # Testing GUI
    main()