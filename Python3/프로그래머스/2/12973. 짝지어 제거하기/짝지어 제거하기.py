def solution(s):
    st = []

    for now in s:
        if len(st)==0 or st[-1]!=now:
            st.append(now)
        else:
            st.pop()
    if len(st)==0:
        return 1
    else:
        return 0