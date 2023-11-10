from rcon import Console

console = Console(host='localhost', password='123')
console.command('serverchat SpikeRocketAdmin: test')
console.close()
