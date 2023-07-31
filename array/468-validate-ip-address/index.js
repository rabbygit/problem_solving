const iPv4 = (queryIP) => {
  const address = queryIP.split(".");

  if (address.length !== 4) return false;

  for (const str of address) {
    const ip = parseInt(str);
    if (ip < 0 || ip > 255) return false;
    if (ip.toString() !== str) return false;
  }

  return "IPv4";
};

const iPv6 = (queryIP) => {
  const address = queryIP.split(":");

  if (address.length !== 8) return false;

  const config = "0123456789abcdefABCDEF";
  for (const str of address) {
    if (str === "" || str.length > 4) return false;
    for (const s of str) {
      if (!config.includes(s)) return false;
    }
  }

  return "IPv6";
};

const validIPAddress = function (queryIP) {
  return iPv4(queryIP) || iPv6(queryIP) || "Neither";
};
