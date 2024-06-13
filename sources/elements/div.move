module shtml::div {

    use std::option::{Self};
    use std::string::{Self, String};
    use std::vector::{Self};

    use sui::vec_set::{Self, VecSet};
    use sui::transfer::{Receiving};

    public struct Div has key, store {
        id: UID,
        children: vector<ID>
    }

    public fun create(
        ctx: &mut TxContext,
    ): Div {
        let div = Div {
            id: object::new(ctx),
            children: vector::empty(),
        };

        div
    }

    public fun add_child<T: key + store>(
        div: &mut Div,
        child: T,
        index: u64,
    ) {
        div.children.insert(object::id(&child), index);
        transfer::public_transfer(child, object::uid_to_address(&div.id));
    }

    public fun swap_child(
        div: &mut Div,
        e1: u64,
        e2: u64
    ) {
        div.children.swap(e1, e2);
    }

    public fun remove_child<T: key + store>(
        div: &mut Div,
        child_to_receive: Receiving<T>,
    ): T {
        let child = transfer::public_receive(&mut div.id, child_to_receive);

        child
    }
}