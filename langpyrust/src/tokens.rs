#![allow(dead_code)]
#[derive(Debug)]
pub enum Tokens {
    //Newline,
    Id {value: String},
    Op {value: String},
    Value {value: String},
    Null,

}