use::std::path::Path;
use::std::fs::File;
use std::io::{self, BufReader, BufRead};

fn parse_input(path: &str) -> Result<io::Split<BufReader<File>>, io::Error>  {
    let input_path = Path::new(&path);
    let file = File::open(input_path)?;

    Ok(io::BufReader::new(file).split(b','))
}


fn check_patterns_in_number(number: i64) -> bool {
    // convert number into str_number.
    let str_num = number.to_string();
    let str_num_len = str_num.len();

    for i in 0..str_num_len/2 {
        let pattern = &str_num[0..i+1];

        if str_num_len % pattern.len() == 0{
            let number_of_chunks = str_num_len / pattern.len(); 

            for j in 0..number_of_chunks {
                let offset = (i + 1) * j;
                let chunk = &str_num[offset..i+offset+1];

                if pattern != chunk {
                    break;
                } else if j == number_of_chunks -1 {
                    return true;
                }
            }
        }
    }
    false
}

fn part_2() {
    let split_input_itr = parse_input("./input/input_1.txt")
        .expect("The file coluld not be open");

    let mut tot = 0;

    for id_range in split_input_itr {
        if let Ok(range) = id_range {
            // parsing
            let range_str = String::from_utf8(range)
                .unwrap();
            let mut range_iter = range_str.split("-");

            let l_num_str = range_iter.next().unwrap();
            let u_num_str = range_iter.next().unwrap();

            let l_num = l_num_str.parse::<i64>().unwrap();
            let u_num = match u_num_str.parse::<i64>() {
                Ok(n) => n,
                Err(_) => {
                    u_num_str
                        .trim_end()
                        .parse::<i64>()
                        .unwrap()
                }
            };
            // end of parsing 
            for n in l_num..u_num+1 {
                if check_patterns_in_number(n) {
                    tot += n;
                }
            }        
        }
    }
    println!("tot: {tot}");

}


fn part_1(){
    let split_input_itr = parse_input("./input/input_1.txt")
        .expect("The file coluld not be open");

    let mut n_len;
    let mut mid_len;
    let mut tot = 0;

    for id_range in split_input_itr {
        if let Ok(range) = id_range {
            // parsing
            let range_str = String::from_utf8(range)
                .unwrap();
            let mut range_iter = range_str.split("-");

            let l_num_str = range_iter.next().unwrap();
            let u_num_str = range_iter.next().unwrap();

            let l_num = l_num_str.parse::<i64>().unwrap();
            let u_num = match u_num_str.parse::<i64>() {
                Ok(n) => n,
                Err(_) => {
                    u_num_str
                        .trim_end()
                        .parse::<i64>()
                        .unwrap()
                }
            };
            // end of parsing
           
            for n in l_num..u_num+1 {
                let n_str = &n.to_string();
                n_len = n_str.len();
                
                if n_len % 2 == 0 {
                    mid_len = n_len/2;  
                    let (first_half, last_half) = n_str.split_at(mid_len);
                    if first_half == last_half {
                        tot += n;
                    }
                }
            }        
        }
    }
    println!("tot: {tot}");
}


fn main() {
    part_2();
}
