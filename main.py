import re
from flask import Flask, render_template, request
from forms import RegisterForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/get-started", methods = ['GET', 'POST'])
def get_started():
    form = RegisterForm()
    if request.method == 'POST':
        if form.is_submitted():
            result = request.form
            return render_template('success.html')
        return render_template('get-started.html', form=form)
    if request.method == 'GET':
        return render_template('get-started.html', form=form)

@app.route("/nfts")
def nfts():
    collection_name = [ 
                   '3landers',
                   'tubby cats',
                   'invisible friends',
                   'bored ape yacht club',
                   'mfers',
                   'nft worlds',
                   'azuki',
                   'starcatchers',
                   'clone x-x takashi murakami',
                   'mutant ape yacht club',
                   'the doggies (snoop dogg)',
                   'worldwide webb land',
                   'cryptopunks',
                   'howlerz',
                   'rtfkt-mnlth',
                   'catblox genesis collection',
                   'doodles',
                   'the sandbox',
                   'degen toonz collection',
                   'dooggies',
                   'karafuru',
                   'soulz monogatari',
                   'cool cats nft',
                   'sunmiya club official',
                   'tales of tsuki genesis',
                   'pixelmon-generation 1',
                   'adidas originals into the metaverse',
                   'acrocalypse',
                   'skuxxverse pass',
                   'tasty bones xyz',
                   'cool pets nft',
                   'metroverse',
                   'g.rilla official',
                   'bunny buddies',
                   'meta toy dragonz',
                   'toxic ape official',
                   'syltare,freezed',
                   'women tribe nft',
                   'syltare-official',
                   'the meta kongz',
                   'genesis bloodshed bears',
                   'byoland',
                   'kaiju mutants nft',
                   'llamaverse genesis',
                   'infinite realm official',
                   'the mfer chicks',
                   'onchainmonkey',
                   'gray boys',
                   'cyberfrogz',
                   "coolman's universe"
                ]

    contract_id = [
                   '0xb4d06d46a8285f4ec79fd294f78a881799d8ced9',
                   '0xca7ca7bcc765f77339be2d648ba53ce9c8a262bd',
                   '0x59468516a8259058bad1ca5f8f4bff190d30e066',
                   '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d',
                   '0x79fcdef22feed20eddacbb2587640e45491b757f',
                   '0xbd4455da5929d5639ee098abfaa3241e9ae111af',
                   '0xed5af388653567af2f388e6224dc7c4b3241c544',
                   '0x69b9c98e8d715c25b330d0d4eb07e68cbb7f6cfc',
                   '0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b',
                   '0x60e4d786628fea6478f785a6d7e704777c86a7c6',
                   '0xc7df86762ba83f2a6197e1ff9bb40ae0f696b9e6',
                   '0xa1d4657e0e6507d5a94d06da93e94dc7c8c44b51',
                   '0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb',
                   '0x40cf6a63c35b6886421988871f6b74cc86309940',
                   '0x86825dfca7a6224cfbd2da48e85df2fc3aa7c4b1',
                   '0x86c35fa9665002c08801805280ff6a077b23c98a',
                   '0x8a90cab2b38dba80c64b7734e58ee1db38b8992e',
                   '0x5cc5b05a8a13e3fbdb0bb9fccd98d38e50f90c38',
                   '0x19b86299c21505cdf59ce63740b240a9c822b5e4',
                   '0x59468516a8259058bad1ca5f8f4bff190d30e066',
                   '0xd2f668a8461d6761115daf8aeb3cdf5f40c532c6',
                   '0xa5c807a62cd6774d6bf518dd2dec0ae17446ad8d',
                   '0x1a92f7381b9f03921564a437210bb9396471050c',
                   '0x8f5aa6b6dcd2d952a22920e8fe3f798471d05901',
                   '0x33a237b384b7065c815f7c745d73a0acf140449c',
                   '0x32973908faee0bf825a343000fe412ebe56f802a',
                   '0x28472a58a490c5e09a238847f66a68a47cc76f0f',
                   '0xd73acd7f5099fdd910215dbff029185f21ffbcf0',
                   '0x19350eb381ab2f88d274e740bd062ab5ff15542e',
                   '0x1b79c7832ed9358e024f9e46e9c8b6f56633691b',
                   'c0x86c10d10eca1fca9daf87a279abccabe0063f247',
                   '0x0e9d6552b85be180d941f1ca73ae3e318d2d4f1f',
                   '0x3f635476023a6422478cf288ecaeb3fdcf025e9f',
                   '0x91cc3844b8271337679f8c00cb2d238886917d40',
                   '0x46dbdc7965cf3cd2257c054feab941a05ff46488',
                   '0xe50c9ba45bc554d76ecc2fc102ec20eb8d738885',
                   '0xe2dd65c215089dda1695ae96cce77f301a1750e5',
                   '0x916fb29aa1a560c4540401b30c8199611d3a1809',
                   '0x6b8f71aa8d5817d94056103886a1f07d12e78ce5',
                   '0x5a293a1e234f4c26251fa0c69f33c83c38c091ff',
                   '0x9d8826881a2beab386a7858e59c228a85b3963e1',
                   '0x0616a2ef54bad0b37dce41c8d8e35cce17a926f3',
                   '0x83f82414b5065bb9a85e330c67b4a10f798f4ed2',
                   '0x9df8aa7c681f33e442a0d57b838555da863504f3',
                   '0x7509615baf2f9d2ee3274bda6cc1fc444e0488e8',
                   '0xda858c5183e9024c0d5301ee85ae1e41dbe0f880',
                   '0x960b7a6bcd451c9968473f7bbfd9be826efd549a',
                   '0x8d4100897447d173289560bc85c5c432be4f44e4',
                   '0xdccc916bf4a0186065f4d1e5b94176f4d17b8c42',
                   "0xa5c0bd78d1667c13bfb403e2a3336871396713c5"
    ]
    return render_template("nfts.html" , collection_name=collection_name, contract_id=contract_id)

@app.route("/about")
def about():
    return render_template("about.html")