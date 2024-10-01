def main():

    with open(__file__, "r") as self:
        code = self.read()

    for i in range(1):
        file_name = f"file{i}.py"
        directory = "SelfPropagation"
        with open(directory+"/"+file_name, "w") as f:
            f.write(code)
    
    print("ファイルの作成が完了しました")

if __name__ == "__main__":
    main()