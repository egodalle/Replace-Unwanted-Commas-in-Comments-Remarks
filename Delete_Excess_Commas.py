import regex as re

def del_excess_commas(input_file,
                      output_file):
                      
    file1 = open(output_file,"w")
    lines = []
    line_num = 0
    excess_commas_cnt = 0
    
    with open(input_file) as f:
        lines = f.readlines()

    for rowdata in lines:
        excess_commas = rowdata.count(",") - 7 # The expected number of delimiter is 7. If this returns 0 then the number of delimiter is correct
        line_num += 1
        if excess_commas == 0:
            file1.write(rowdata)
        else:
            for i in range(excess_commas):
                rowdata = re.sub(r'^(.*?(,.*?){6}),', r'\1', rowdata) # This regex will delete the 6th comma
                excess_commas_cnt += 1
            file1.write(rowdata)
            print("The line number with incorrect commas is {}".format(line_num))
    print ("The total number of corrected commas in the comments is {}:".format(excess_commas_cnt))
    print("The total number of record is {}:".format(line_num))
            
input_file = 'C:/Python/Excess_Delimiter.csv'
output_file = 'C:/Python/Updated_Delimiter.csv'

del_excess_commas(input_file,
                    output_file)