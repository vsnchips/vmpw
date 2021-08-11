
/*
#[no_mangle]
pub extern "C" fn hello(_in: &i32) -> i32 {
    println!("Hello from Rust through wasm");
    _in + 1
   
}
*/

#[no_mangle]
pub extern "C" fn add_one(x: &i32) -> i32 {
    x + 1
}


use wasm_bindgen::prelude::*;
//#[no_mangle]
#[wasm_bindgen]
pub fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}


#[macro_use] extern crate gl;
use gl::*;
//#[wasm_bindgen]
#[no_mangle]
pub extern "C" fn draw() -> () {
    // ...platform-specific OpenGL setup...

    println!("Repaint!\n");
    unsafe {
        gl::ClearColor(0.,0.,1.,0.5 );
        gl::Clear(gl::COLOR_BUFFER_BIT);
    }

    
}

