# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"G64z111","system":"readv2"},{"code":"10504.0","system":"med"},{"code":"15019.0","system":"med"},{"code":"15252.0","system":"med"},{"code":"16517.0","system":"med"},{"code":"23671.0","system":"med"},{"code":"24446.0","system":"med"},{"code":"25615.0","system":"med"},{"code":"26424.0","system":"med"},{"code":"27975.0","system":"med"},{"code":"3149.0","system":"med"},{"code":"33543.0","system":"med"},{"code":"34758.0","system":"med"},{"code":"36717.0","system":"med"},{"code":"39403.0","system":"med"},{"code":"40758.0","system":"med"},{"code":"47642.0","system":"med"},{"code":"5185.0","system":"med"},{"code":"5363.0","system":"med"},{"code":"53745.0","system":"med"},{"code":"5602.0","system":"med"},{"code":"569.0","system":"med"},{"code":"57495.0","system":"med"},{"code":"6155.0","system":"med"},{"code":"8837.0","system":"med"},{"code":"91627.0","system":"med"},{"code":"94482.0","system":"med"},{"code":"9985.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ischaemic-stroke-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ischaemic-stroke---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ischaemic-stroke---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ischaemic-stroke---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
