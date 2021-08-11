from wasmer import engine, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler

#Compile a rust file to wasm
    
# Let's define a default store, that holds the engine, that holds the compiler.
store = Store(engine.JIT(Compiler))

def buildExports(filename,store=store):
    return buildInstance(filename,store).exports

def buildModule(filename,store=store):
    cmd = f'rustc {filename} --crate-type=cdylib --codegen opt-level=3 --target=wasm32-unknown-unknown -o {filename}.wasm'
    os.system(f"echo {cmd}")
    os.system(cmd)
    
    # Let's compile the module to be able to execute it!
    return Module(store, open(f'{filename}.wasm', 'rb').read())
     
def buildInstance(filename,store=store):
    # Now the module is compiled, we can instantiate it.
    module=buildModule(filename,store)
    return Instance(module)
    
def exportsFromWasm(filename,store=store):
    return Instance(Module(store,open(filename, 'rb').read())).exports
