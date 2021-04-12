mod tokens;

use std::error::Error;
use std::io::prelude::*;
use std::fs::File;
use std::path::Path;

fn main() {

    let path = Path::new("test.pr");
    let display = path.display();

    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),

        Ok(file) => file,
    };

    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),

        Ok(_) => println!("{} contains:\n{}", display, s),
    }

    lexer(s)
}

fn lexer(program: String) {

    let mut tree: Vec<tokens::Tokens> = parse_tokens(program);

    run_program(tree);

}

fn parse_tokens(program: String) -> Vec<tokens::Tokens>{
    let mut parsed = program.split_whitespace();
    let mut vec: Vec<tokens::Tokens> = Vec::new();

    for token in parsed {
        match token {
            "null" => vec.push(tokens::Tokens::Null),
            "printf" => vec.push(tokens::Tokens::Id {value: token.to_string()}),
            "<=" | ">=" | "<" | ">" | "=" | "==" | "+" | "-" | "/" | "*" | "%" | "^" => vec.push(tokens::Tokens::Op {value : token.to_string()}),
            _ => vec.push(tokens::Tokens::Value {value: token.to_string()}),
        }
    }

    println!("{:?}", vec);
    vec

}

fn run_program(tree: Vec<tokens::Tokens>) {

    for token in tree {
        match token {
            tokens::Tokens::Id{value} => continue,
            _ => continue,

        }
    }
}