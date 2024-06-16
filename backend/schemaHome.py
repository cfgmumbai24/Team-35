#  export const dataset = [
#    {
#    "id": 1,
#   "title": "Student Loan",
#    "link": "https://www.youtube.com/embed/X4HcuMtu5zc",
#    "steps": "Step 1: Research and compare different loan options.\nStep 2: Fill out the Free Application for Federal Student Aid(FAFSA).\nStep 3: Receive your Student Aid Report(SAR) and review it for accuracy.\nStep 4: Wait for your school's financial aid office to send an award letter.\nStep 5: Review and accept the loan terms in the award letter.\nStep 6: Complete entrance counseling to ensure you understand the loan terms.\nStep 7: Sign the Master Promissory Note (MPN) to legally agree to repay the loan.\nStep 8: Your school will certify your enrollment status and loan amount.\nStep 9: The loan funds are disbursed to your school to pay for tuition and fees.\nStep 10: Any remaining funds are given to you for other educational expenses.",
#    "extLinks": "https://example.com/student-loan-details"
#    },
#    {
#    "id": 2,
#    "title": "Home Loan",
#    "link": "https://www.youtube.com/embed/OVoMUPw4ukg",
#    "steps": "Step 1: Check your credit score.\nStep 2: Determine how much you can afford.\nStep 3: Save for a down payment.\nStep 4: Get pre-approved for a loan.\nStep 5: Shop for the best mortgage rates.\nStep 6: Choose a lender and apply for the loan.\nStep 7: Provide necessary documentation (income, employment, etc.).\nStep 8: Get the home appraised.\nStep 9: Complete the underwriting process.\nStep 10: Close the loan and sign the final documents.",
#    "extLinks": "https://example.com/home-loan-details"
#    },
#    {
#    "id": 3,
#    "title": "Business Loan",
#    "link": "https://www.youtube.com/embed/KwoYlqQV2-g",
#    "steps": "Step 1: Assess your business needs and loan purpose.\nStep 2: Review your credit score and financial history.\nStep 3: Gather necessary documentation(business plan, financial statements).\nStep 4: Research and compare lenders and loan options.\nStep 5: Complete the loan application.\nStep 6: Submit the application along with required documents.\nStep 7: Await lender's review and approval process.\nStep 8: Respond to any additional information requests from the lender.\nStep 9: Review loan terms and sign the agreement.\nStep 10: Receive funds and implement your business plans.",
#    "extLinks": "https://example.com/business-loan-details"
#    },
#    {
#    "id": 4,
#    "title": "Account Creation",
#    "link": "https://www.youtube.com/embed/Tjx4QQE-I0k",
#   "steps": "Step 1: Choose a bank and type of account.\nStep 2: Gather necessary documents (ID, proof of address, etc.).\nStep 3: Visit the bank's branch or website.\nStep 4: Fill out the account application form.\nStep 5: Submit your documents and application form.\nStep 6: Wait for the bank to process your application.\nStep 7: Verify your identity if required.\nStep 8: Deposit the minimum required amount if applicable.\nStep 9: Receive your account details (account number, debit card, etc.).\nStep 10: Start using your new bank account.",
#    "extLinks": "https://example.com/vehicle-loan-details"
#   },
#   {
#   "id": 5,
#   "title": "Cash Withdraw",
#   "link": "https://youtube.com/embed/gi_3QwohaiE",
#   "steps": "Step 1: Go to your bank or ATM.\nStep 2: Insert your debit card into the machine.\nStep 3: Enter your PIN number.\nStep 4: Select 'Withdraw' from the menu.\nStep 5: Choose the account type (Checking/Savings).\nStep 6: Enter the amount you wish to withdraw.\nStep 7: Confirm the amount.\nStep 8: Collect your cash from the machine.\nStep 9: Take your receipt.\nStep 10: Remove your debit card and secure it.",
#   "extLinks": "https://example.com/vehicle-loan-details"
#   },
#   {
#   "id": 6,
#   "title": "Income Tax",
#   "link": "https://www.youtube.com/embed/qCfGsQYINKc",
#   "steps": "Step 1: Determine your total income from all sources.\nStep 2: Identify any applicable deductions and exemptions.\nStep 3: Calculate your taxable income by subtracting deductions from total income.\nStep 4: Use the current tax rate to compute your tax liability.\nStep 5: Check for any eligible tax credits to reduce your tax liability.\nStep 6: Collect all necessary documents such as W-2s, 1099s, and receipts.\nStep 7: Complete the appropriate tax forms (e.g., 1040 in the U.S.).\nStep 8: Review your tax return for accuracy.\nStep 9: Submit your tax return by the deadline, usually April 15 in the U.S.\nStep 10: Pay any taxes owed or arrange for a refund if you overpaid.",
#   "extLinks": "https://example.com/vehicle-loan-details"
#      },
#   ];


{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the content item"
        },
        "title": {
          "type": "string",
          "description": "Title of the content item"
        },
        "link": {
          "type": "string",
          "format": "uri",
          "description": "Link to the associated video or external resource"
        },
        "steps": {
          "type": "string",
          "description": "Detailed steps or instructions related to the content item"
        },
        "extLinks": {
          "type": "string",
          "format": "uri",
          "description": "Link to additional external resources or details"
        }
      },
      "required": ["id", "title", "link", "steps", "extLinks"]
    }
  }
