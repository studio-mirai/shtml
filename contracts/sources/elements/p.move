module shtml::p {

    use std::string::{String};
    use std::type_name::{Self, TypeName};
    
    use sui::transfer::{Receiving};

    public struct P has key, store {
        id: UID,
        content: String, 
    }

    public fun create(
        content: String,
        ctx: &mut TxContext,
    ): P {
        let p = P {
            id: object::new(ctx),
            content: content,
        };

        p
    }

    public(package) fun id(
        p: &P
    ): ID {
        object::id(p)
    }
}