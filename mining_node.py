from blockchain import create_genesis_block, create_new_block, Block

def mine_block(node_id, block):
    print(f"Node {node_id} is mining block...")
    block.mine_block()
    print(f"Node {node_id} successfully mined block {block.index} with hash: {block.hash}")

if __name__ == "__main__":
    genesis_block = create_genesis_block()
    new_block = create_new_block(genesis_block)
    mine_block(1, new_block)
