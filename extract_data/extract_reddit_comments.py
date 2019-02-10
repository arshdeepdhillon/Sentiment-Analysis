"""
Data: Reddit json files aquired from here http://files.pushshift.io/reddit/comments/
"""

import json  # for reading list of json objects
import os

class Extract:

    def __init__(self):

        # raw reddit data is store in this folder
        self.raw_path = "../raw_data/"
        # self.raw_path = "__test__Raw Data/"


        # once each raw data file is formatted into a json format, it is store under json_formatted_path folder
        self.json_formatted_path = "json_formatted_data/"


        # all comments from each file that resides in json_formatted_path folder is
        # extracted and aggregated into one file under comments_parsed_path folder
        self.comments_parsed_path = "comments_extracted/"

        self.parsed_files = {}


    def getData(self):
        """Purpose is to format the raw reddit data into a json like format.

        Returns a dictonary of properly formatted json data.
        """

        # for each file in Raw Data
        for data_file in os.listdir(self.raw_path):
            with open(self.raw_path + data_file) as f:

                # read the whole file
                s = f.readlines()

            # strip empy space and put commas on the ends of each line
            s = [line.replace("\n", ",\n") for line in s if len(line) > 1]
            s[-1] = s[-1].replace("},", "}")


            if not os.path.isdir(self.json_formatted_path):
                os.mkdir(self.json_formatted_path)

            # write the formatted json data into data_file
            with open(self.json_formatted_path + data_file, "w") as f:
                f.write('{\n"comments":[\n')

                for line in s:
                    f.write(line)
                f.write("]\n}")

        return (self.getListOfDicData())


    def getListOfDicData(self):
        """Purpose is to take all the formatted files in json_formatted_path and map the file name to its json data.

        Returns a dictonary where the key is file name and value is its json data (ie (filename.txt, jsonData)).
        """

        for parsed_data in os.listdir(self.json_formatted_path):
            with open(self.json_formatted_path + parsed_data) as f:
                L = json.load(f)
                self.parsed_files[parsed_data] = L

        return (self.parsed_files)


    def getComments(self):
        """Purpose is to extract reddit comments from all the files and format it into an easly accessable json format.

        This function extracts comments from all the raw files and puts it into a single file which is created in comments_parsed_path.

        Returns nothing.

        """

        if not os.path.isdir(self.json_formatted_path):
            dicList = self.getData()
        else:
            dicList = self.getListOfDicData()

        # print(dicList['smallDataSet.txt']['comments'][0]['body'])

        if not os.path.isdir(self.comments_parsed_path):
            os.mkdir(self.comments_parsed_path)

        try:
            import string
            with open(self.comments_parsed_path + "output.txt", "w") as f:
                # print(dicList)

                # for each formatted file...
                for _, dicComments in dicList.items():
                    # print(type(dicComments))

                    # for each "comments" object ( in this case there will always be one "comments" )...
                    for _, values in dicComments.items():
                        # print(type(values))

                        # for each comment in the array, write its body to the file
                        for comment in values:

                            s = comment["body"].strip().replace("\n", "")

                            printable = set(string.printable)
                            for chr in filter(lambda x: x in printable, s):
                                f.write(chr)

                            f.write("\n")

        except Exception as e:
            with open(self.comments_parsed_path + "output.txt", "a") as f:
                f.write("**ERROR MESSAGE: encoding issue**" + str(e))




# uncomment the below lines to run the program

'''redditComments = Extract()
redditComments.getComments()'''



# uncomment the below lines to print method's description
# print(Extract.getData.__doc__)
# print(Extract.getListOfDicData.__doc__)
# print(Extract.getComments.__doc__)
