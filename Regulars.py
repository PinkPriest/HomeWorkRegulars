from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

# def find_similar()
with open("C:\\Users\\mi17n\\Downloads\\phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  new_contacts_list = [{
    'lastname': '',
    'firstname': '',
    'surname': '',
    'phone': '',
  }]
  for row in contacts_list:
    row_copy = " ".join(row[:3])
    lastname = row_copy.split(" ")[0]
    firstname = row_copy.split(" ")[1]
    for new_row in new_contacts_list:
      print()
    surname = row_copy.split(" ")[2]
    phone_pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})( \(?(\D{4}) (\d+)\)?)?"
    phone_sub = r"+7(\2)\3-\4-\5 \7\8"
    phone = row[5]
    phone = re.sub(phone_pattern, phone_sub, phone)
    if phone.endswith(" "):
      phone = phone[:-1]
    for new_row in new_contacts_list:
      print()
    new_contacts_list.append([{
    'lastname': lastname,
    'firstname': firstname,
    'surname': surname,
    'phone': phone,
  }])
  pprint(new_contacts_list)



with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)