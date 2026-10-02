use std::path::Path;
use std::io::{BufReader, BufRead};
use std::fs::File;

fn get_max_number(str: String) -> u32{
    let mut ten = 0;
    let mut unit = 0;
    let mut number;
    let mut i = 0;

    let char_itr = str.chars();
    for char_number in char_itr {
        number = char_number.to_digit(10)
            .unwrap();

        if number > ten && i < str.len() - 1{
            ten = number;
            unit = 0;
        } else if number > unit {
            unit = number; 
        }
        i += 1;
    }

    ten*10 + unit
}

fn get_max_number_p2(str: String, n: usize) -> u32{
    let mut num_veq = vec![0u32; n];
    let mut number;
    let mut i = 0;
    let mut concat_num = 0u32;

    let char_itr = str.chars();
    for char_number in char_itr {
        number = char_number.to_digit(10)
            .unwrap();

        for j in 0..num_veq.len() {
            if number > num_veq[j] {
                num_veq[j] = number;
//i = 14 j = 0 
                if i < str.len() - (n-1) - j {
                    for k in j+1..n {
                        num_veq[k] = 0;
                    }
                }
                break;
            }

            for x in &num_veq {
                print!("{x} ");
            }
            println!();
        }
        i += 1
    }

    for j in 0..n {
        let exp: u32 = (n - 1 - j).try_into().unwrap(); // n es usize
        concat_num += num_veq[j] * (10u32.pow(exp));
    } 
    concat_num
}

fn part_1(){
   let input_path = Path::new("./../input/input_1.txt");
   let file = File::open(&input_path).expect("The path does not exist");
   let file_buff = BufReader::new(&file);

   let mut tot = 0; 
   for line in file_buff.lines().map(|l| l.unwrap()) {
       tot += get_max_number(line);
   } 
   println!("{tot}");
}


fn part_2(){
   let input_path = Path::new("./../input/input_1.txt");
   let file = File::open(&input_path).expect("The path does not exist");
   let file_buff = BufReader::new(&file);

   let tot = get_max_number_p2("234234234234278".to_string(), 2);
   println!("{tot}");
}


fn main() {
    part_2();
}
