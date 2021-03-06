"""Rttov interface

Must be copied into the port/interface directory for each atmospheric plugin
and then updated.
"""

# Paths
DATA_DIR = 'data'
PROFILE_DIR = 'profiles'

# Keys
keys = [
        'downwell',
        'upwell',
        'tau',
        'wavenums',
        'extra',
    ]

# Updates
"""Updates must be made per-plugin."""
def get_downwell(rttov_obj):
    """Change the -1 to : for all layers."""
    return rttov_obj.Rad2Down[:,:,-1]
def get_upwell(rttov_obj):
    """Same option as above."""
    return rttov_obj.Rad2Up[:,:,-1]
def get_tau(rttov_obj):
    return rttov_obj.TauTotal
def get_wnums(rttov_obj):
    return rttov_obj.WaveNumbers
def get_extra(rttov_obj):
    skin_temp = rttov_obj.Profiles.Skin[0,0]
    output = [skin_temp]
    return output
                
get_fromKey = {
        keys[0]: get_downwell,
        keys[1]: get_upwell,
        keys[2]: get_tau,
        keys[3]: get_wnums,
        keys[4]: get_extra,
    }
