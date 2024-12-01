use std::fs::read_to_string;

fn main() {
    println!("Hello, world!");

    let filename = "input.txt";

    let mut va: Vec<i32> = Vec::new();
    let mut vb: Vec<i32> = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        let s: Vec<&str> = line.split_whitespace().collect();

        let a: i32 = s[0].parse().expect("Not a valid number");
        let b: i32 = s[1].parse().expect("Not a valid number");

        va.push(a);
        vb.push(b);
    }

    va.sort();
    vb.sort();

    let merged: Vec<i32> = va.into_iter().zip(vb.into_iter())
                            .map( |(x,y)| (x - y).abs() )
                            .collect();

    let total: i32 = merged.into_iter().sum();

    println!("{total}");
}
