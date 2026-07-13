use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod greet_rune {
    use pyo3::prelude::*;

    /// Prints a greeting for Rune.
    #[pyfunction]
    fn greet() {
        println!("Hi Rune!");
    }
}
