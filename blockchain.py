#Tasks: 1) create block; 2) create blockchain; 3) print blockchain

#generates timestamps
import datetime
#contains hashing algorithms
import hashlib

#TASK 1

#defining the 'block' data structure
class Block:
    #each block has 7 attributes 
  
    #1 number of the block
    blockNo = 0
    #2 what data is stored in this block?
    data = None
    #3 pointer to the next block
    next = None
    #4 the hash of this block (serves as a unique ID and verifies its integrity)
    #a hash is a function that converts data into a number within a certain range. 
    hash = None
    #5 a nonce is a number only used once  
    nonce = 0
    #6 store the hash (ID) of the previous block in the chain
    previous_hash = 0x0
    #7 timestamp 
    timestamp = datetime.datetime.now()

    #initialize a block by storing some data in it
    def __init__(self, data):
        self.data = data

    #Function to compute 'hash' of a block
    #a hash acts as both a unique identifier & verifies its integrity
    #if someone changes the hash of a block
    #every block that comes after it is changed 
    #this helps make a blockchain immutable
    def hash(self):
        #SHA-256 is a hashing algorithm that
        #generates an almost-unique 256-bit signature that represents
        #some piece of text
        h = hashlib.sha256()
        #the input to the SHA-256 algorithm
        #will be a concatenated string
        #consisting of 5 block attributes
        #the nonce, data, previous hash, timestamp, & block#
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        #returns a hexademical string
        return h.hexdigest()

    def __str__(self):
        #print out the value of a block
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"


#TASK2

#defining the blockchain datastructure
#consists of 'blocks' linked together to form a 'chain'. That's why it's called 'blockchain'
class Blockchain:
    
    #mining difficulty
    diff = 10
    #2^32. This is the maximum number we can store in a 32-bit number
    maxNonce = 2**32
    #target hash, for mining
    target = 2 ** (256-diff)

    #generates the first block in the blockchain
    #this is called the 'genesis block'
    block = Block("Genesis")
    #sets it as the head of our blockchain
    head = block

    #adds a given block to the chain of blocks
    #the block to be added is the only parameter
    def add(self, block):
        
        #set the hash of a given block as our new block's previous hash
        block.previous_hash = self.block.hash()
        #set the block # of our new block
        #as the given block's # + 1, since it's next in the chain
        block.blockNo = self.block.blockNo + 1

        #set the next block equal to itself
        #this is the new head of the blockchain
        self.block.next = block
        self.block = self.block.next

    #determines whether or not we can add a given block to the blockchain
    def mine(self, block):
        #from 0 to 2^32 
        for n in range(self.maxNonce):
            #is the value of the given block's hash less than our target value?
            if int(block.hash(), 16) <= self.target:
                #if it is,
                #add the block to the chain
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


#TASK3

#initialize blockchain
blockchain = Blockchain()

#mine 5 blocks
for n in range(5):
    blockchain.mine(Block("Block " + str(n+1)))
    
#print out each block in the blockchain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next