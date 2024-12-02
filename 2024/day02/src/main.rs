use std::fs::read_to_string;

fn main() {
    let filename = "input.txt";
    let mut fnd : i32 = 0;

    for line in read_to_string(filename).unwrap().lines() {
        let s: Vec<&str> = line.split_whitespace().collect();

        let mut deltas : Vec<i32> = Vec::new();
        let mut signs : Vec<bool> = Vec::new();

        for i in 1..s.len(){
            // I want the scala type yield here...
            // Or python list comprehension.
            let cur: i32 = s[i].parse().expect("Not a number");
            let prev:i32 = s[i-1].parse().expect("Not a number");

            deltas.push( ( cur-prev).abs() );
            signs.push( ( cur-prev) >= 0 );
        }

        // Check the level differences

        let a = signs.iter().fold(true, |res,x| res & x);
        let b = signs.iter().fold(true, |res,x| res & !x);

        let sign = a|b;

        let cor = *deltas.iter().max().unwrap() < 4 && *deltas.iter().min().unwrap() > 0 && sign;

        if cor {
            fnd +=1;
        }
    }

    println!("Part 0: {fnd}");
}
