use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn part_1(period: i32,  initial_state: i32){
    let mut tot = 0;
    let mut cur = initial_state;
    let mut a: i32;

    // Read file
    let input_path = Path::new("./src/input_1");
    let file = File::open(&input_path)
        .expect("Error: the file {input_path.display()} coudl not be open");
 
    let lines = io::BufReader::new(&file)
        .lines()
        .map_while(Result::ok);    
    //

    for mut line in lines{
        let str_value = line.split_off(1);
        let mut number = str_value.parse::<i32>()
            .expect("Error: the value {str_value} could not be parse");

        if line == "L" {
            number *= -1;
        }
        
        a = cur+number;
        cur = a.rem_euclid(period);
        if cur == 0 {
            tot += 1;
        } 
    }
    println!("tot: {tot}");
}

fn part_2(period: i32,  initial_state: i32){
    let mut tot = 0;
    let mut cur = initial_state;
    let mut step;

    // Read file
    let input_path = Path::new("./src/input_1");
    let file = File::open(&input_path)
        .expect("Error: the file {input_path.display()} coudl not be open");
 
    let lines = io::BufReader::new(&file)
        .lines()
        .map_while(Result::ok);    
    //

    for mut line in lines{
        let str_value = line.split_off(1);
        let number = str_value.parse::<i32>()
            .expect("Error: the value {str_value} could not be parse");

        if line == "L" {
            step = -1;
        } else {
            step = 1;
        }

        for _ in 0..number {
            cur += step;

            if cur == -1 {
                cur = 99;
            } else if cur == 100 {
                cur = 0
            }

            if cur == 0 {
                tot += 1;
            }
        }        
    }
    println!("tot: {tot}");
}

fn main() {
    let period = 100;
    let initial_state = 50;
    part_1(period, initial_state);
    part_2(period, initial_state);
}
