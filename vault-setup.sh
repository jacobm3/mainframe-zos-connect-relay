vault policy write sudo-admin - <<EOF

path "*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}

EOF

 vault auth enable userpass
 vault write auth/userpass/users/jacob \
    password=foo \
    policies=db1,sudo-admin
