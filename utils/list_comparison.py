def compare_lists(list1, list2):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)

    # Find differences
    diff_in_list1 = set1 - set2
    diff_in_list2 = set2 - set1

    # Print the differences
    print("Items in list1 but not in list2:", diff_in_list1)
    print("Items in list2 but not in list1:", diff_in_list2)

# Example usage
list1 = ["Account_Group","CFOP_Category","CO_Name","Central_Billing_Block","Central_Deletion_Block","Central_Deletion_Flag","Central_Delivery_Block","Central_Order_Block","Central_Posting_Block","Central_Sales_Block","Check_Digit","City","City_Postal_Code","Classification","Communication_Type","Country","Customer_Number","District","Ecommerce_Indicator","House_Number","House_Number_Supplement","ICMD_Exempt","Industry_Code_1","Is_Natural_Person","Language","Liable_For_VAT","Location_Code_No_1","Location_Code_No_2","Name1","Name2","Name3","Name4","PO_Box","PO_Box_Postal_Code","Region","Regional_Structure_Grouping","Search_Term1","Search_term2","Street","Street2","Street3","Street4","Street5","SubTrip_Group","Tax_Jurisdiction","Tax_Number_1","Tax_Number_2","Tax_Number_3","Tax_Number_4","Tax_Number_5","Tax_Number_Type","Tax_Type","Trading_Partner","Transportation_Zone","VAT_Registration_Number","Vendor"]
list2 = ["Account_Group","CFOP_Category","CO_Name","Central_Billing_Block","Central_Deletion_Block","Central_Deletion_Flag","Central_Delivery_Block","Central_Order_Block","Central_Posting_Block","Central_Sales_Block","Check_Digit","City","City_Postal_Code","Classification","Communication_Type","Country","Customer_Number","District","Ecommerce_Indicator","House_Number","House_Number_Supplement","ICMD_Exempt","Industry_Code_1","Is_Natural_Person","Language","Liable_For_VAT","Location_Code_No_1","Location_Code_No_2","Name1","Name2","Name3","Name4","PO_Box","PO_Box_Postal_Code","Region","Regional_Structure_Grouping","Search_Term1","Search_Term2","Street","Street2","Street3","Street4","Street5","SubTrip_Group","Tax_Jurisdiction","Tax_Number_1","Tax_Number_2","Tax_Number_3","Tax_Number_4","Tax_Number_5","Tax_Number_Type","Tax_Type","Trading_Partner","Transportation_Zone","VAT_Registration_Number","Vendor"]
compare_lists(list1, list2)
