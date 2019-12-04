#!/bin/bash -eux

function usage {
    cat << EOM
    ./new_day.bash [year] [day_id]
    e.g. ./new_day.bash 2019 one
    will make:
        2019/day_one/
        2019/day_one/one.py
        2019/day_one/test_one.py
        2019/day_one/one_input.txt
    The "day_id" python file will have some boilerplate in them.

EOM
}

if [ $# -le 1 ]; then
    usage
    exit 1
elif [[ $# == "--help" || $# == "-h" ]]; then
    usage
    exit 1
fi


year=${1}
day=${2}
day_path="${year}/day_${day}"
mkdir -p "${day_path}"

cat <<EOM > "${day_path}/${day}.py"
import os
this_path = os.path.dirname(__file__)
inpath = os.sep.join([this_path, "${day}_input.txt"])
EOM

> "${day_path}/${day}_input.txt"
> "${day_path}/test_${day}.py"
