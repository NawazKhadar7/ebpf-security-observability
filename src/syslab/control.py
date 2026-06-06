import ipaddress,shlex,subprocess

def update_command(pin,source):
    packed=ipaddress.IPv4Address(source).packed
    return ['bpftool','map','update','pinned',str(pin),'key','hex',*[f'{b:02x}' for b in packed],'value','hex','01']
def plan(interface,object_file):
    if not interface or len(interface)>15 or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.:-' for c in interface):raise ValueError('invalid interface name')
    return ['ip','link','set','dev',interface,'xdp','obj',str(object_file),'sec','xdp']
def describe(command):return shlex.join(command)
