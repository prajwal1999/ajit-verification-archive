import json

def get_end_state():
    with open("files/log/main.log") as log_file:
        lines = log_file.readlines()
        end_state = {}
        for line in lines:
            end_state[line.split()[3].split(',')[0]] = line.split('actual = ')[1].split(' ')[0]
        file = open('coverage/C_model/end_state.json', 'w')
        json.dump(end_state, file)
        file.close()

def read_trace():
    PC_executed = []
    coverage = {}
    with open("files/trace_files/main.C_trace.0") as trace_file:
        lines = trace_file.readlines()
        for idx, line in enumerate(lines):
            if idx >= 2:
                temp_pc = line.split(',')[0][-8:]
                PC_executed.append(hex(int(temp_pc, 16))[2:])
    with open("files/compiled/main/main.objdump") as obj_dump_file:
        lines = obj_dump_file.readlines()
        obj = {}
        for idx, line in enumerate(lines):
            try:
                obj[line.split()[0][:-1]] = line.split()[5]
                coverage[line.split()[5]] = 0
            except:
                pass

    for pc in PC_executed:
        coverage[obj[pc]] += 1
    with open("coverage/C_model/functional.json", 'w') as functional_cov_file:
        json.dump(coverage, functional_cov_file)

if __name__ == "__main__":
    get_end_state()
    read_trace()
