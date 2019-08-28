use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut line_iter = stdin.lock().lines();
    let n_tests: i64 = line_iter.next().unwrap().unwrap().parse().unwrap();
    for i in 0..n_tests {
        let test_line = line_iter.next().unwrap().unwrap();
        let mut splitted_line = test_line.split_whitespace();
        let n: i64 = splitted_line.next().unwrap().parse().unwrap();
        let k: i64 = splitted_line.next().unwrap().parse().unwrap();
        let (max, min) = solve(n, k);
        println!("Case #{}: {} {}", i + 1, max, min)
    }
}

fn solve(n_stalls: i64, mut n_persons: i64) -> (i64, i64) {
    let mut max = n_stalls;
    let mut larger_count = 1;
    let mut smaller_count = 0;
    while n_persons > larger_count + smaller_count {
        n_persons -= larger_count;
        n_persons -= smaller_count;
        let result = divide_all(max, larger_count, smaller_count);
        max = result.0;
        larger_count = result.1;
        smaller_count = result.2;
    }
    divide(max, larger_count, n_persons)
}

fn divide_all(max: i64, larger_count: i64, smaller_count: i64) -> (i64, i64, i64) {
    if max % 2 == 0 {
        return (max / 2, larger_count, larger_count + smaller_count * 2);
    } else {
        (
            (max - 1) / 2,
            larger_count * 2 + smaller_count,
            smaller_count,
        )
    }
}

fn divide(max: i64, larger_count: i64, n_persons: i64) -> (i64, i64) {
    if n_persons <= larger_count {
        if max % 2 == 0 {
            (max / 2, max / 2 - 1)
        } else {
            ((max - 1) / 2, (max - 1) / 2)
        }
    } else {
        if max % 2 == 0 {
            (max / 2 - 1, (max - 1) / 2)
        } else {
            ((max - 1) / 2, (max - 1) / 2 - 1)
        }
    }
}
