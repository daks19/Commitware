import os
import random
import string
import subprocess
import time

def generate_random_text(length=12):
    """Generates a random alphanumeric string."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    # Get the absolute path of the script currently running
    script_path = os.path.abspath(__file__)
    
    # Randomly choose between 5 or 6 iterations
    num_commits = random.randint(6,7)
    print(f"Starting {num_commits} automated commits for {os.path.basename(script_path)}...\n")

    for i in range(num_commits):
        random_text = generate_random_text()
        
        # 1. Modify the file by appending a comment with the random text
        with open(script_path, "a") as file:
            file.write(f"\n# Auto-generated string: {random_text}")
        
        try:
            # 2. Stage the modified file
            subprocess.run(["git", "add", script_path], check=True, capture_output=True)
            
            # 3. Commit the changes
            commit_message = f"Automated commit {i+1}/{num_commits}: Added {random_text}"
            subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True)
            
            print(f"[{i+1}/{num_commits}] Successfully committed with text: {random_text}")
            
            # Pause briefly to ensure commit timestamps are distinct
            time.sleep(1)
            
        except subprocess.CalledProcessError as e:
            print("Git add/commit failed. Are you in an initialized git repository?")
            print(f"Error details: {e.stderr.decode('utf-8').strip()}")
            return  # Exit the script early if committing fails

    # 4. Push the new commits to the remote repository
    print("\nPushing commits to remote repository...")
    try:
        subprocess.run(["git", "push"], check=True, capture_output=True)
        print("Successfully pushed to remote!")
    except subprocess.CalledProcessError as e:
        print("Git push failed. Do you have a remote configured and an upstream branch set?")
        print("You may need to run: git push -u origin <branch-name>")
        print(f"Error details: {e.stderr.decode('utf-8').strip()}")

if __name__ == "__main__":
    main()
# Auto-generated string: nQKxrhWusKwX
# Auto-generated string: xi6UUlrZtQ41
# Auto-generated string: ZRFYtsSz4Fga
# Auto-generated string: xfVM4jPHm7kP
# Auto-generated string: u8T4EUX6cCf8
# Auto-generated string: ElIzYD23Yogy
# Auto-generated string: GdEiIHvf2fyf
# Auto-generated string: tecgHmwHb1Ti
# Auto-generated string: l8wzBdKRMekz
# Auto-generated string: 2NyNzSykMkaj
# Auto-generated string: e9qkUelQsjEg
# Auto-generated string: 3syDH7ul62k3
# Auto-generated string: sIreOjxZSLfX
# Auto-generated string: 9WVMGQiMlpIE
# Auto-generated string: rg0jF3C2rmBb
# Auto-generated string: L65xbnBsMXTV
# Auto-generated string: mHcPA9wsQLKT
# Auto-generated string: x3sYWBUlhhZk
# Auto-generated string: i8m1i04SxdGi
# Auto-generated string: TXTRNcFqwon9
# Auto-generated string: 8OPOKkBSOW6h
# Auto-generated string: n8PIqHWYotiQ
# Auto-generated string: M8LQv8kXVYoK
# Auto-generated string: v3PlfO3jvh3g
# Auto-generated string: ZLhFhjG2ZHSE
# Auto-generated string: y9zY3NxaLHLc
# Auto-generated string: hVMzMJV2yE4m
# Auto-generated string: 6ZpcZLGpNmY2
# Auto-generated string: 72LJa2afrmqK
# Auto-generated string: eomto3epXn0I
# Auto-generated string: 7pdXj8t9DEBz
# Auto-generated string: D0YWskTPT9nJ
# Auto-generated string: Wj1QpgtEW9IV
# Auto-generated string: WmUySxIfxajm
# Auto-generated string: EfkF5QXvgqUi
# Auto-generated string: 9L0WT8C8gAzc
# Auto-generated string: vnCTJMIB0c8O
# Auto-generated string: dFhM0vh5uZk4
# Auto-generated string: sHuHO4l3AW4t
# Auto-generated string: Wpxt32G3sAG3
# Auto-generated string: cOGSlnzjyCGv
# Auto-generated string: wXSlzZ3xEUOr
# Auto-generated string: KsRRVAvzL15g
# Auto-generated string: Z3ILuMaFDqwY
# Auto-generated string: UoeAaxZ39jgs
# Auto-generated string: kke2vZiys53u
# Auto-generated string: Bpp5mNyYCdkd
# Auto-generated string: E1thYmFwAp5A
# Auto-generated string: dMZG9sxkJWOr
# Auto-generated string: 3YtczHuqH0SS
# Auto-generated string: YFqabKxdQvuz
# Auto-generated string: B92JaL5oemOL
# Auto-generated string: iaAsEpzArIJq
# Auto-generated string: 7Y1vZXKSbeEc
# Auto-generated string: 8N3u6XPHPRKi
# Auto-generated string: r6kN4SGZKk6z
# Auto-generated string: H3h34Ivrna4o
# Auto-generated string: y05Tn88SMKOI
# Auto-generated string: fqsy0UojZCg9
# Auto-generated string: 2EwpqswFJM8R
# Auto-generated string: xsoP4TqSvLx1
# Auto-generated string: K6AfvJeehDHY
# Auto-generated string: wT91O9UYiLov
# Auto-generated string: Q0WETFLzJmAM
# Auto-generated string: l8cjaxOhJRjt
# Auto-generated string: fTlU6BTt0UVj
# Auto-generated string: vj53v2kRY0w5
# Auto-generated string: VGPX43N89t6t
# Auto-generated string: PZvYyN9fFOsk
# Auto-generated string: fiHnzFJiWdlc
# Auto-generated string: vh0lRpwSKuxh
# Auto-generated string: YnerwDB5pwFq
# Auto-generated string: HdtdmCo5lIQt
# Auto-generated string: n6GXkVV0K2zf
# Auto-generated string: GHO1cjNeA2sr
# Auto-generated string: xdFazPAO4ciC
# Auto-generated string: sQs2gWrBBFDg
# Auto-generated string: fx8ojsJNZpvd
# Auto-generated string: 31MSBZe2CMyX
# Auto-generated string: pR2aMrY3BUy6
# Auto-generated string: 41rtG3IAkMn8
# Auto-generated string: CCdo1Wla5rv0
# Auto-generated string: MB9PEAecOxFq
# Auto-generated string: pUXzOSR9x6Ki
# Auto-generated string: rFGP0uf09Nc4
# Auto-generated string: gXxvd89AK0vF
# Auto-generated string: ItAt55fvmPfk
# Auto-generated string: KWTqip86tcGY
# Auto-generated string: SJPSW0LKr4E1
# Auto-generated string: mzSNlGlORDsw
# Auto-generated string: h35tcUm9cDgQ
# Auto-generated string: tH3cKLcXDmzI
# Auto-generated string: c1gLBnt1cflA
# Auto-generated string: W5VdV6O76cLT
# Auto-generated string: meq71HP0s249
# Auto-generated string: 6f1CVWXxNT53
# Auto-generated string: tV1E0itftbNQ
# Auto-generated string: 8YYYJwLUAkjP
# Auto-generated string: 0L5RmTaaPnph
# Auto-generated string: Qa8zJBbkPowD
# Auto-generated string: 5yHfB2Jmi2Fi
# Auto-generated string: UekIF0PVAVcp
# Auto-generated string: QNvB1YpiPEGk
# Auto-generated string: cjVyINx8U0Zk
# Auto-generated string: 1u9FaA18Yfoc
# Auto-generated string: mvkdgOFVOwfH
# Auto-generated string: AiizLXJzlPlC
# Auto-generated string: e4oZpHlrC9DD
# Auto-generated string: ywQvaBkGgDCZ
# Auto-generated string: EYl7W9EtN8Qc
# Auto-generated string: 69o1U6UE2mJo
# Auto-generated string: TNIsVgs4QYBO
# Auto-generated string: V2Gt6FsfFMCo
# Auto-generated string: xyVX74UQeldL
# Auto-generated string: FZGnN0tqjcgl
# Auto-generated string: FDGTqSRi7w8g
# Auto-generated string: Iqo1gzQt4Umd
# Auto-generated string: tl97tZdf1Cs1
# Auto-generated string: k8D8Hgh1PMaQ
# Auto-generated string: oDBFVdMMGa5G
# Auto-generated string: bxigGf3wuDdy
# Auto-generated string: 8VfWO7qgg2Fw
# Auto-generated string: BpBczuOIrVmB
# Auto-generated string: LjAFviJq38uM
# Auto-generated string: Ppr9i2kTTd2G
# Auto-generated string: 9438rKErduPN
# Auto-generated string: ycxpgyNEwnNO
# Auto-generated string: Yu9A2za1x3R2
# Auto-generated string: 70rDg9yZrs0F
# Auto-generated string: R4GiQuwGx7T9
# Auto-generated string: ZhFOtU9XVYjy
# Auto-generated string: 3J6uf56wGXSm
# Auto-generated string: B3zga1bjchAC
# Auto-generated string: 0iK3oOZSAFqG
# Auto-generated string: 57RI1sYRLm4U
# Auto-generated string: bFKcT5910Xag
# Auto-generated string: GDbaRaJV0uDa
# Auto-generated string: fyVtrTW0bRfO
# Auto-generated string: GvrUFH27RpQv
# Auto-generated string: GdSKKt2IIRgh
# Auto-generated string: aCnDSW96sePI
# Auto-generated string: EMF9Xps0o8pB
# Auto-generated string: yuQ0PxI8rpat
# Auto-generated string: 3KErPrTzuQp4
# Auto-generated string: 9NVMC8kWl7Gt
# Auto-generated string: fP3EFlMlJ2ns
# Auto-generated string: iPNeaZeC9kfY
# Auto-generated string: TjtQdr7sSrH9
# Auto-generated string: 7TKpxgkfnLwy
# Auto-generated string: 5UspznK542Zk
# Auto-generated string: GnKlEl6lgJPL
# Auto-generated string: 0gGcFGsBp4TY
# Auto-generated string: WkT3f2FjxclF
# Auto-generated string: pKYNgfcHFJOa
# Auto-generated string: p3pFdDn462U4
# Auto-generated string: fSIcUg8i67pg
# Auto-generated string: CnByyBNRwmd4
# Auto-generated string: BopHh6apLvNO
# Auto-generated string: vJ6iXjEG8c59
# Auto-generated string: qcLahCacjvn9
# Auto-generated string: fOinLpXCCsC7
# Auto-generated string: uou08SajKvAF
# Auto-generated string: CeX4FuhreiH1
# Auto-generated string: EKYAIZFAujIu
# Auto-generated string: JPmsC3JrkVUN
# Auto-generated string: 9R90580hz3aF
# Auto-generated string: AheRaDCNzDTH
# Auto-generated string: pmDRe4XjTZru
# Auto-generated string: ki6uMLG98XVe
# Auto-generated string: rdzkjm7pzzZ7
# Auto-generated string: CusnbL6lzlb3
# Auto-generated string: v07fLb4AGTiV
# Auto-generated string: tlWXX0wEfbRj
# Auto-generated string: xEpzf4NTnt0M
# Auto-generated string: zw0S807dCP7w
# Auto-generated string: 58MIth9qiGQO
# Auto-generated string: HwyqZpMvPCwS
# Auto-generated string: ipwMYW6IUg6K
# Auto-generated string: 7GrypIaUmwtK
# Auto-generated string: ifw42YKrxmv6
# Auto-generated string: 3dysQAGwvI2V
# Auto-generated string: wrJKBb2hSMWi
# Auto-generated string: eL4MQNCuQi4Z
# Auto-generated string: F1ufTMr80ji9
# Auto-generated string: wGlV46dEakiC
# Auto-generated string: MwJzwuGYnuiT
# Auto-generated string: 9iBbG77D40pu
# Auto-generated string: rS1qiWS9Fw61
# Auto-generated string: JGpP50ffIf3H
# Auto-generated string: zpwi3S6sdmf0
# Auto-generated string: P1pV2cVSWuS0
# Auto-generated string: e2R4dDVSTXlY
# Auto-generated string: lI9OO88lLozN
# Auto-generated string: ge3U3GR1LWOI
# Auto-generated string: ZmPdKNHN2KwA
# Auto-generated string: tNsetLhWP2KZ
# Auto-generated string: jubTaraOHA0q
# Auto-generated string: G8EEcZY15TEq
# Auto-generated string: XnpshbkiZ0pY
# Auto-generated string: Sqn0XniTEIR5
# Auto-generated string: nGj5DsEF0OGX
# Auto-generated string: ymbjwL3DbIHo
# Auto-generated string: raNNRjxIOKyi
# Auto-generated string: lFcd0nJiPPw2
# Auto-generated string: L0xAVaRJFdGO
# Auto-generated string: HLmvHUiq9I8s
# Auto-generated string: QYtbNlKMaae6
# Auto-generated string: msaLCvQ3uLdK
# Auto-generated string: EkGHdoUPvztE
# Auto-generated string: uqIC8E51kmvx
# Auto-generated string: MlGSSEBI5hyL
# Auto-generated string: 297hBgvtUjqs
# Auto-generated string: Go8M7EyBKfmZ
# Auto-generated string: Zof7VAsOc861
# Auto-generated string: AZwIJXovPLUL
# Auto-generated string: SviHQfoJ4clE
# Auto-generated string: YNfrNPM3wIjR
# Auto-generated string: gXTSRzx6P14m
# Auto-generated string: 4wJ56INkFtqx
# Auto-generated string: gfeTRRoE2a4D
# Auto-generated string: QWBplk9kRhpJ
# Auto-generated string: igU8fdia1eSg
# Auto-generated string: NxQUuvtwXQtK
# Auto-generated string: EnnOBW51Gklq
# Auto-generated string: MngPYAhbWKc9
# Auto-generated string: sryrXSp2OAEW
# Auto-generated string: XIAtDSJqkM4U
# Auto-generated string: jvyaH15ZbCp0
# Auto-generated string: NVK4lIkgOtLV
# Auto-generated string: MJ7iKZdguPVO
# Auto-generated string: 5Lb7cIhLWwAL
# Auto-generated string: tG7oxLPCu52z
# Auto-generated string: lOo4HCIKU4DZ
# Auto-generated string: toElqoRE7Ptm
# Auto-generated string: SAodw2ZjkyKe
# Auto-generated string: QFFAQdGeRYyz
# Auto-generated string: zEUnvjOMzoez
# Auto-generated string: yX91hkCHziH6
# Auto-generated string: i0R2QpxteUdm
# Auto-generated string: Mw5HRfFXM6UO
# Auto-generated string: ba2W7sTWIgel
# Auto-generated string: 96s7OsFSBVbp
# Auto-generated string: GCZ9WbNvT0GA
# Auto-generated string: uXPtJ7MX2K6G
# Auto-generated string: yj6a5CWuiny8
# Auto-generated string: g2hpbwLF2Fki
# Auto-generated string: hJ2ILvPTNwrO
# Auto-generated string: eIjC4sVPVrOQ
# Auto-generated string: IHQ6MNuv2YTm
# Auto-generated string: s2fbkC2zjW40
# Auto-generated string: J0wT7ZKKq7aO
# Auto-generated string: 298XEAnM7tYD
# Auto-generated string: nkJXtsOUUXpy
# Auto-generated string: KBLrUJClQj0X
# Auto-generated string: RmDIPxSTEipk
# Auto-generated string: SiT009jPGZEl
# Auto-generated string: UYlV0npIyT9O
# Auto-generated string: RC7za8HgaS3H
# Auto-generated string: EfzLzTAUpbL5
# Auto-generated string: guDp9LjFCett
# Auto-generated string: GZlDplTv0ocI
# Auto-generated string: soDGiOdwkTU9
# Auto-generated string: U5TyBJdF9wYe
# Auto-generated string: KKpGelJg1UKG
# Auto-generated string: nbkkmXpFPQsf
# Auto-generated string: POFmIcwJo9AA
# Auto-generated string: NdKrJiacFzeJ
# Auto-generated string: x6GI67ZXCLC2
# Auto-generated string: LpaGc91tJU1m
# Auto-generated string: Mre1rGtNMayf
# Auto-generated string: XpdC3saMECet
# Auto-generated string: WhBNAyoUuJek
# Auto-generated string: QZ5UoGZG9eGr
# Auto-generated string: gLIQWAX7Fbok
# Auto-generated string: L9JqWj9ZVGI6
# Auto-generated string: xIerYsYb9Ecc
# Auto-generated string: rk223mx0QGCG
# Auto-generated string: 8st4cTuy8zME
# Auto-generated string: RGqDAe7cnNVX
# Auto-generated string: qIKqYHtEzS8t
# Auto-generated string: 5dLgsawLwmZB
# Auto-generated string: LwRGhWZ2GCXq
# Auto-generated string: Nf7g5i5xii7q
# Auto-generated string: sBUZSKJrmHCc
# Auto-generated string: kD1wOJAQS40I
# Auto-generated string: W8qZJxRQJXag
# Auto-generated string: mOEdnsH82MKt
# Auto-generated string: Prrec0qhYVBb
# Auto-generated string: T5ACOMWFmb6M
# Auto-generated string: yux4yDN1ZesJ
# Auto-generated string: Khnr0UWnD35A
# Auto-generated string: iI009DmAP0yK
# Auto-generated string: gwnOdBmnv9Zp
# Auto-generated string: DdfrLuIiYgp8
# Auto-generated string: gkS81eTVbPd7
# Auto-generated string: EXgqMVEsYZno
# Auto-generated string: wW8moaiHvsDz
# Auto-generated string: VM4QVkOXCVgp
# Auto-generated string: Kpyadh5v6WPK
# Auto-generated string: e6TrBXHl4xP2
# Auto-generated string: pfS4uxoSwC7a
# Auto-generated string: 0DJ9bAX7f5Sw
# Auto-generated string: 7IU6IZghgPkp
# Auto-generated string: JTxP0FxxFho7
# Auto-generated string: sjMgGovZt5zF
# Auto-generated string: YK5n7Tz15IIc
# Auto-generated string: etegLOpnUUjI
# Auto-generated string: IB5yiDAynjyG
# Auto-generated string: b0eIMDiOvzGD
# Auto-generated string: n8LqShmCa9MM
# Auto-generated string: pHyTfb97DP3k
# Auto-generated string: RcAAa1HI9X8P
# Auto-generated string: k9ppUcxiHPs7
# Auto-generated string: 7grCE94e5Ien
# Auto-generated string: ENjvsDfteXSr
# Auto-generated string: 4zzGE8pBV5Df
# Auto-generated string: 9xLnhQ2pC5bD
# Auto-generated string: bxuShZN0g2zb
# Auto-generated string: gGdlYURkgCX3
# Auto-generated string: 2hEksPCvVgDJ
# Auto-generated string: LS7iGxBWUd0o
# Auto-generated string: nQ4vzH3moeZ8
# Auto-generated string: 5t3JpFIpvep2
# Auto-generated string: 63a3mhGOhGUt
# Auto-generated string: pZpdNLsqdRx6
# Auto-generated string: NKDKXZH9wblT
# Auto-generated string: zZQYnzzU9lfM
# Auto-generated string: JLw51V4t1HMS
# Auto-generated string: xmWxbXvnEe6h
# Auto-generated string: dQ5Mjb8b2Llf
# Auto-generated string: es9kbGYoPHB6
# Auto-generated string: O2VJ1QU919xT
# Auto-generated string: IW7qa6s6DFHm
# Auto-generated string: rnlHqzzgtDPB
# Auto-generated string: tMYLtFU6iXYt
# Auto-generated string: YD6TueN0yTP0
# Auto-generated string: FQmEoVvHmNP0
# Auto-generated string: mKjkD3D3j2sB
# Auto-generated string: hZn6UKw2yWV8
# Auto-generated string: pl9T57zRYYHJ