from stackoverflow.StackOverFlow import StackOverFlow
from stackoverflow.Tags import Tags


def main():
    instance = StackOverFlow.get_instance()
    user = instance.add_user("Sai Kowshik", "askowshik@outlook.com")
    instance.add_question("This is a sample question",[Tags.SCIENCE],user.id)
    for i in instance.search("sample"):
        print(i.content)

if __name__ == "__main__":
    main()