users:
  # 2000 - 2010 UID reserved for various dedicated users
  read:
    uid: 2000
    class: read
  admin:
    uid: 2001
    class: admin
  operations:
    uid: 2002
    class: operations
  salt:
    uid: 2003
    sshkeys:
      - ssh-rsa AAA
  {%- if grains.get('os') == 'eos' %}
  gnmic:
    uid: 2004
    password:
      type: sha512
      value: AAA
  {%- endif %}
  # Hoomans
  username:
    uid: 2010
    sshkeys:
      - ssh-ed25519 AAA
      - ssh-rsa AAA
