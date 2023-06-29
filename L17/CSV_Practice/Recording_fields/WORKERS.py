import csv

outfile = open("worker_ip_job_title.csv", 'w')
outfile_header = "First Name, Last Name, Job Title, IP\n"
outfile.write(outfile_header)
with open("worker.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for row in reader:
        first_name = row[0]
        last_name = row[1]
        address = row[2]
        company_name = row[3]
        job_title = row[4]
        ip = row[5]
        print(first_name, last_name, address, company_name, job_title, ip)
        line = f"{first_name},{last_name},{job_title},{ip}\n"
        outfile.write(line)

    outfile.close()