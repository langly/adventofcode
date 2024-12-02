use std::fs::read_to_string;
use std::collections::HashMap;

fn main() {
    let filename = "input.txt";

    let mut va: Vec<i32> = Vec::new();
    let mut vb: Vec<i32> = Vec::new();

    let mut counts: HashMap<i32,i32> = HashMap::new();

    for line in read_to_string(filename).unwrap().lines() {
        let s: Vec<&str> = line.split_whitespace().collect();

        let a: i32 = s[0].parse().expect("Not a valid number");
        let b: i32 = s[1].parse().expect("Not a valid number");

        if !counts.contains_key(&b) {
            counts.insert(b,0 as i32);
        }

        let cnt = counts.get(&b).unwrap() + 1;
        counts.insert(b, cnt);

        va.push(a);
        vb.push(b);
    }

    va.sort();
    vb.sort();

    let merged: Vec<i32> = va.iter().zip(vb.iter())
                            .map( |(x,y)| (x - y).abs() )
                            .collect();

    let total: i32 = merged.into_iter().sum();
    println!("Part 0 : {total}");

    // Now part 1
    let mut part2: i32 = 0;

    for item in va{
        let v = counts.get(&item);

        if v.is_some() {
            let part = item * v.unwrap();
            part2 += part;
        }

    }

    println!("Part 1: {part2}");


}
