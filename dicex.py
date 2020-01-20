phone_dic = {
    "Alice": "703-493-1834",
    "bob": "857-384-1234",
    "elize": "484-584-2923",
}
print(phone_dic["elize"])
phone_dic["Kareem"] = "938-489-1234"
phone_dic["bob"] = "968-345-2345"

del phone_dic["Alice"]
print(phone_dic)