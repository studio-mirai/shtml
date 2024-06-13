module shtml::div {

    use std::option::{Self};
    use std::string::{Self, String};
    use std::type_name::{Self, TypeName};
    use std::vector::{Self};

    use sui::object_bag::{Self, ObjectBag};
    use sui::vec_set::{Self, VecSet};
    use sui::transfer::{Receiving};

    use shtml::p::{Self, P};

    public struct Div has key, store {
        id: UID,
        children: ObjectBag,
        count: u64,
        order: vector<ID>,
    }

    public fun create(
        ctx: &mut TxContext,
    ): Div {
        let div = Div {
            id: object::new(ctx),
            children: object_bag::new(ctx),
            count: 0,
            order: vector::empty(),
        };

        div
    }

    public fun delete(
        div: Div,
    ) {
        let Div {
            id,
            children,
            count: _,
            order,
        } = div;

        children.destroy_empty();
        order.destroy_empty();
        id.delete();
    }

    public fun add_child<T: key + store>(
        child: T,
        div: &mut Div,
    ) {
        assert!(!div.order.contains(&object::id(&child)));
        div.order.push_back(object::id(&child));
        div.children.add(object::id(&child), child);
        div.count = div.count + 1;
    }

    public fun remove_child<T: key + store>(
        child_id: ID,
        div: &mut Div,
    ): T {
        div.count = div.count - 1;
        div.children.remove(child_id)
    }

    public fun swap_children(
        child1: u64,
        child2: u64, 
        div: &mut Div,
    ) {
        div.order.swap(child1, child2);
    }
}