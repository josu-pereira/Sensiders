
package hashingmac;

import java.io.UnsupportedEncodingException;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Hashmac {
        
    private String macAddress;
    
    public Hashmac() throws UnknownHostException, SocketException, NoSuchAlgorithmException, UnsupportedEncodingException {
        InetAddress localhost = InetAddress.getLocalHost();
        NetworkInterface ni = NetworkInterface.getByInetAddress(localhost);
        byte[] hardwareAddress = ni.getHardwareAddress();
        
        String[] hexa = new String[hardwareAddress.length];
        for (int i = 0; i < hardwareAddress.length; i++) {
             hexa[i] = String.format("%02X", hardwareAddress[i]);
        }
        
        String address = String.join("",hexa);
        Long mac2 = Long.parseLong(address,16);
        
        macAddress = mac2.toString();
        
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] encodedhash;
        encodedhash = digest.digest(macAddress.getBytes(StandardCharsets.UTF_8));
        StringBuilder hexString = new StringBuilder(2 * encodedhash.length);
        for (int i = 0; i < encodedhash.length; i++) {
            String hex = Integer.toHexString(0xff & encodedhash[i]);
            if(hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        
        macAddress = hexString.toString();
    }
    
    public String getMacAddress() {
        return macAddress;
    }

    public void setMacAddress(String macAdress) {
        this.macAddress = macAdress;
    }
}
