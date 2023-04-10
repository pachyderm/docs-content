import subprocess

def main():
    warnings = 0 
    errors = 0 
    files = subprocess.run(["pachctl", "list", "file", "datum-batching-log-counter@master"])
    for file in files:
        with open('/pfs/logs/' + file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'WARN' in line:
                    warnings += 1
                if 'ERR' in line:
                    errors += 1
    write_results(warnings, errors)

# create a results.txt file and write the total warnings and errors.

def write_results(warnings, errors):
    with open('/pfs/out/results.txt', 'w') as f:
        f.write('Warnings: ' + str(warnings) + '\n')
        f.write('Errors: ' + str(errors))

print("User code is starting")
subprocess.run(["pachctl", "connect", "grpc://localhost:1650"])

print("starting while loop")
while True:
    subprocess.run(["pachctl", "next", "datum"])
    print("next datum called")

    main()