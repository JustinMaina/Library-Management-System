import sys
from book_management import add_book, get_all_books, update_book_copies, delete_book
from member_management import add_member, get_all_members, delete_member
from borrow_management import borrow_book, return_book

def print_help():
    print("Usage:")
    print("  python main.py <command> <arguments>")
    print("Commands:")
    print("  book add <title> <author> <copies>")
    print("  book list")
    print("  book update <book_id> <new_copies>")
    print("  book delete <book_id>")
    print("  member add <name> <email>")
    print("  member list")
    print("  member delete <member_id>")
    print("  borrow <book_id> <member_id>")
    print("  return <borrow_id>")
    print("  help")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "book":
        subcommand = sys.argv[2]
        if subcommand == "add":
            title = sys.argv[3]
            author = sys.argv[4]
            copies = int(sys.argv[5])
            add_book(title, author, copies)
            print("Book added")
        elif subcommand == "list":
            books = get_all_books()
            for book in books:
                print(f"{book.id}: {book.title} by {book.author} {book.copies} copies")
        elif subcommand == "update":
            book_id = int(sys.argv[3])
            new_copies = int(sys.argv[4])
            update_book_copies(book_id, new_copies)
            print("Book copies updated")
        elif subcommand == "delete":
            book_id = int(sys.argv[3])
            delete_book(book_id)
            print("Book deleted")

    elif command == "member":
        subcommand = sys.argv[2]
        if subcommand == "add":
            name = sys.argv[3]
            email = sys.argv[4]
            add_member(name, email)
            print("Member added")
        elif subcommand == "list":
            members = get_all_members()
            for member in members:
                print(f"{member.id}: {member.name} - Email: {member.email}")
        elif subcommand == "delete":
            member_id = int(sys.argv[3])
            delete_member(member_id)
            print("Member deleted")

    elif command == "borrow":
        book_id = int(sys.argv[2])
        member_id = int(sys.argv[3])
        borrow_book(book_id, member_id)
        print("Book borrowed")

    elif command == "return":
        borrow_id = int(sys.argv[2])
        return_book(borrow_id)
        print("Book returned")

    else:
        print_help()

if __name__ == "__main__":
    main()
