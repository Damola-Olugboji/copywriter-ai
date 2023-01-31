from models import v1
import ast
import time, os, sys

class Article:
    def __init__(self, output_filename):
        self.output_filename = output_filename
        if os.path.isfile(f"./{output_filename}"):
            os.remove(f"./{output_filename}")
        

    def title(self, article_title):
        self.save_to_file(article_title)

    def introduction(self, theme):
        res = v1.prompt_model("you're an very well connected individual with the ability to call various industry experts to help you: your goal is below: \n",
            f"create a list for an article titled: {theme} but put the reasons in a python list"
        )
        start = res.find("[")
        end = res.rfind("]")
        self.res_list = res.strip()[start-2:end]
        print(self.res_list + "\n")
        flag = input("do you want to continue: ")
        if flag == "0":
            sys.exit()
        
        prompt = f"you're an experienced copywriter and content creator. Write a introduction paragraph to an article titled below, the reasons are here {self.res_list} - dont include all the reasons in the introduction!: \n"
        res = v1.prompt_model(prompt, theme)
        print(res)
        self.save_to_file(res)
        print("Introduction finished...")
        
        flag = input("do you want to continue: ")
        if flag == "0":
            sys.exit()

    def mainbody(self, theme):
        
        content_list = ast.literal_eval(self.res_list.strip())

        time.sleep(3)

        for topic in content_list:
            prompt = f"you're an accomplished writer and copywriter, write a paragraph for the topic: {topic} as it fits in the article titled {theme}"
            res = v1.free_model(prompt)
            self.save_to_file("\n" + topic)
            self.save_to_file(res)
            time.sleep(3)
        print("Body finished...")

        
    def conclusion(self, theme):
        res = v1.free_model(f"you're an accomplished writer and copywriter, write a closing paragraph for an article titled {theme}, with the reasons {self.res_list} ")
        self.save_to_file("\n" + res)
        
        print("Conclusion finished...")

        
    def save_to_file(self, text):
        with open(self.output_filename, "a+") as file:
            file.write(text)


def main():
    article_title = "5 Reasons to buy gold"
    test = Article("./articles/gold_buying.txt")
    
    test.introduction(article_title)
    time.sleep(5)
    test.mainbody(article_title)
    time.sleep(5)
    test.conclusion(article_title)


if __name__ == "__main__":
    main()
