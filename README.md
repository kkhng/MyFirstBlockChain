#### A simple project to understand BlockChain Mining. I learned it from a Big Data Analysis course I took back in the year 2018.

### Tasks:

###### 1. Create Block
###### 2. Create BlockChain
###### 3. Print BlockChain


#### Codes: [https://github.com/kkhng/MyFirstBlockChain]( https://github.com/kkhng/MyFirstBlockChain)

#### Below is a summary I wrote based on my understanding to the White Paper [Nakamoto, Satoshi. (2009). Bitcoin: A Peer-to-Peer Electronic Cash System. Cryptography Mailing list at [https://metzdowd.com](https://metzdowd.com)]

#### If you are interested to know more, you can download the original paper from this link: [https://bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf) 

In general, the main benefit brought by peer-to-peer electronic cash system is an enhanced mechanism which allows the practice of transactions precluding double-spending without the involvement of the so-called trusted third parties (i.e. the financial institutions, the banks).

Transactions in this system required to be publicly announced. Each owner will hold a public and private keys. Public key can be shared with everyone and is used for encryption purpose, using for verification. While private key is personally owned which is used for decryption, using for signature creation. For instance, each owner can transfer a coin to the next by digitally signing a hash of the previous transaction and the public key of the next owner, and adding these to the end of the coin. 

In terms of network working, all new transactions in the system are first broadcasted to all nodes. Continuously, each node will collect the new transactions into a block, also the node will work on finding the difficult proof-of-work for its block. The node will then broadcast its block to all the other nodes when it found the difficult proof-of-work for the block. Noting that the nodes will only accept the block when all transactions in the block are valid and not already spent. The nodes will continue work on creating the next block to indicate that they accepted the current block into the chain by using the hash of the accepted block as the previous hash. The nodes will keep extending the longest chain which they consider it as the correct one. But in the case of having two nodes broadcasting simultaneously, nodes will work on the first one they received and save the other branch. The extension will keep going on whenever a new proof-of-work is found, shifting works will happen with the nodes selecting longer branch continuing the extension of the chain. 

Some additional explanation to the paragraph above, proof-of-work is a system used to implement a distributed timestamp server on a peer-to-peer basis. It involves scanning a hashed value with the hash has to begin with a number of zero bits. It works with accreting a nonce in the block until a value is found that gives the block’s hash the required zero bits. While, timestamp server refers to an important function required to get the transacted data recorded with time proven. Each timestamp includes the previous timestamp in its hash and that of forming a connected chain. Noting that proof-of-work is essentially one-CPU-one-vote. The majority decision is represented by the longest chain which was created during the process of accumulating proof-of-work searches. 

Majority CPU power is controlled by honest nodes, inducing honest chain to be the fastest and could outpace the other competing chains. Therefore, to modify a past block, an attacker would have to redo the proof-of-work of the block and all blocks after it and then catch up with and surpass the work of the honest nodes. Mathematically proven, the probability for the attacker to be able to catch up from n blocks behind dropped exponentially when the number of the blocks which attacker has to catch up with increased. 

The system also incorporates with transaction fees as incentive to stop people from violating the rules. Incentive value is the difference between the output and input value of the transaction. In addition, due to the transaction is hashed in the Merkle Tree, with only the root included in the block’s hash helps easing the disk space issue. In terms of payment verification, a user only needs to keep a copy of the block headers of the longest proof-of-work chain through querying network nodes, which helps keep the hassle of running a full network node. Verification usually reliable as long as the network controlled by honest nodes. If it happens to be that an attacker has overpowered the network, one strategy to protect against is to accept alert from the network nodes when they detect an invalid block. Privacy issue has also taken into consideration by this system, in which by keeping the public key anonymous. Meaning, the public can see someone sending an amount of coins to another one, but they couldn’t know who is doing the transaction. But there could be a drawback, whereby a user can fall into the tracking of receiving multiple transactions. If all input transactions from the others were owned by a same owner. This would lead to the risk of information leakage of the others if the owner’s key is revealed. 

