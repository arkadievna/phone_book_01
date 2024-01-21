import text
import view
import model

def find_contact():
    word = view.input_data(text.input_search_word)
    result = model.find_contact(word)
    view.show_contacts(result, text.contacts_not_found(word))

def start_app():
    while True:
        choice = view.main_menu()
# В этой старой версии метод match не работает, выдаёт ошибку.
# В новой версии это будет работать:
        # match choice:
        #     case 1:
        #         model.open_file()
        #     case 2:
        #         pass
        #     case 3:
        #         pass
        #     case 4:
        #         pass
        #     case 5:
        #         pass
        #     case 6:
        #         pass
        #     case 7:
        #         pass
        #     case 8:
        #         break

# в старой версии так:
        if choice == 1:
                  model.open_file()
                  view.print_message(text.load_successful)
        elif choice == 2:
                  model.save_file()
                  view.print_message(text.save_successful)
        elif choice == 3:
                  pb = model.phone_book
                  view.show_contacts(pb, text.empty_phone_book)
        elif choice == 4:
                  contact = view.add_contact(text.new_contact)
                  model.new_contact(contact)
                  view.print_message(text.new_contact_added_successful(contact[0]))
        elif choice == 5:
            find_contact()
        elif choice == 6:
            find_contact()
            pb = model.phone_book
            c_id = int(view.input_data(text.input_id_change_contact))
            c_contact = view.add_contact(text.change_contact, pb[c_id])
            model.change_contact(c_id, c_contact)
            view.print_message(text.contact_changed_successful(c_contact[0]))
        elif choice == 7:
            find_contact()
            c_id = int(view.input_data(text.input_id_delete_contact))
            name = model.delete_contact(c_id)[0]
            view.print_message(text.contact_delete_successful(name))
        elif choice == 8:
            view.print_message(text.good_bay)
                  break




